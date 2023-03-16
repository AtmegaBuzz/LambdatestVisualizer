import { useState,useEffect,useContext } from "react";
import { LogsContext } from "../App";
import LogCard from "../components/LogCard";



export default function Logs(){

    const {networkLogs,setNetworkLogs,filterKey,filterValue} = useContext(LogsContext);
    const [matchAll,setMatchAll] = useState("");

    const get_network_logs = async ()=>{
        if (matchAll!==""){
            let resp = await fetch(`http://127.0.0.1:8000/logs?key=%20&val=%20&multiMatch=${matchAll}`)
            let data = await resp.json();
            setNetworkLogs(data);
        }
        else{
            let resp = await fetch(`http://127.0.0.1:8000/logs?key=${filterKey}&val=${filterValue}`)
            let data = await resp.json();
            setNetworkLogs(data);
        }
    } 

    useEffect(()=>{
        get_network_logs();
    },[filterKey,filterValue,matchAll])

    return( 

        <div className="flex flex-col items-center">
            <div className="w-full h-[100px] justify-center items-center mt-10 flex">
                <input
                    onChange={(val)=>setMatchAll(val.target.value)}
                    type="text"
                    className="block w-[30%] h-[60px] p-2 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    placeholder="Search with Keyword"
                />
            </div>
            {
                networkLogs.map(log=><LogCard key={log._id} log={log}/>)
            }
        </div>

    );
}
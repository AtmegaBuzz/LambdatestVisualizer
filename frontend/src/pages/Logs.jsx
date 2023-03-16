import { useEffect,useContext } from "react";
import { LogsContext } from "../App";
import LogCard from "../components/LogCard";



export default function Logs(){

    const {networkLogs,setNetworkLogs,filterKey,filterValue} = useContext(LogsContext);

    const get_network_logs = async ()=>{
        let resp = await fetch(`http://127.0.0.1:8000/logs?key=${filterKey}&val=${filterValue}`)
        let data = await resp.json();
        setNetworkLogs(data);
    }

    useEffect(()=>{
        get_network_logs();
    },[filterKey,filterValue])

    return( 

        <div className="flex flex-col items-center">
            {
                networkLogs.map(log=><LogCard key={log._id} log={log}/>)
            }
        </div>

    );
}
import { useContext,useEffect } from "react";
import TotalLogs from "../components/Logs";
import { LogsContext } from "../App";

export default function Home(){

    const {setYearLogCount,filterKey,filterValue} = useContext(LogsContext);

    const get_log_count = async () => {
        let resp = await fetch(`http://127.0.0.1:8000?key=${filterKey}&val=${filterValue}`);
        let data = await resp.json();
        setYearLogCount(data);
    };

    useEffect(()=>{
        get_log_count();
    },[]);

    return(

        <TotalLogs />

    );

}
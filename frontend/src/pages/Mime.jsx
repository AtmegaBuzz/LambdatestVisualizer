import { useContext, useEffect } from "react";
import { LogsContext } from "../App";
import MimeLogs from "../components/mimeType";


const get_logs = async (mimeType,fkey,fval)=>{
    
    let resp = await fetch(`http://127.0.0.1:8000/mimeType?key=${fkey}&val=${fval}`, {
        headers: {
            accept: "application/json",
            "Content-Type": "application/json",
        },
        method: "POST",
        body: JSON.stringify({
            mimeType: mimeType,
        }),
        });
        let data = await resp.json();
        return data["count"];
}


export default function Mime() {
  
    const { 
        mimeTypes,
        filterMimeType,
        setMimeTypes,
        setYearMimeTypeLogs,
        setMimePieData,
        setFilterMimeType,
        filterKey,filterValue
    
    } = useContext(LogsContext);


    //  Mime types logs API calls
    const get_mimeTypes = async () => {
        let resp = await fetch("http://127.0.0.1:8000/mimeType");
        let data = await resp.json();
        setMimeTypes(["All",...data]);
        setFilterMimeType("All");
    };

    const get_year_mimetype_logs = async () => {
        
        if(filterMimeType==="All"){

            let resp = await Promise.all(
                mimeTypes.map(async mimeType => {
                    if (mimeType!=="All"){
                        return {
                            mime:mimeType,
                            data: await get_logs(mimeType,filterKey,filterValue)
                        }
                    }

                })
            )
            setYearMimeTypeLogs(resp);
        }

        else{
            setYearMimeTypeLogs([{
                mime:filterMimeType,
                data: await get_logs(filterMimeType)
            }])
        }
    };

    const get_mime_pie_data = async () => {
        let resp = await fetch(`http://127.0.0.1:8000/mimePieData?key=${filterKey}&val=${filterValue}`);
        let data = await resp.json();
        setMimePieData(data);
    };
    // Mime type API call ENDS

    useEffect(() => {
        get_mimeTypes();
    }, []);
    
    useEffect(() => {
        get_mime_pie_data();
        get_year_mimetype_logs();
    }, [filterMimeType,filterKey,filterValue]);

  return <MimeLogs />;
}

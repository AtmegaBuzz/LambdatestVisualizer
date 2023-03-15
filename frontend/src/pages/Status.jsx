import { useContext, useEffect } from "react";
import { LogsContext } from "../App";
import StatusCodeLogs from "../components/statusCode";


const get_logs = async (status) =>{
    let resp = await fetch("http://127.0.0.1:8000/statusCode", {
        headers: {
            accept: "application/json",
            "Content-Type": "application/json",
        },
        method: "POST",
        body: JSON.stringify({
            statusCode: status,
        }),
    });
    let data = await resp.json();
    return data["count"];
}


export default function Status() {

    const {
        statusCodes,
        filterStatusCode,
        setStatusCodes,
        setYearStatusCodeLogs,
        setStatusPieData,
        setfilterStatusCode,
    } = useContext(LogsContext);

    //  Status code logs API calls
    const get_statusCodes = async () => {
        let resp = await fetch("http://127.0.0.1:8000/statusCode");
        let data = await resp.json();
        setStatusCodes(["All",...data]);
        setfilterStatusCode("All");
    };


    const get_year_statuscode_logs = async () => {

        if(filterStatusCode==="All"){

            let resp = await Promise.all(
                statusCodes.map(async status => {
                    if (status!=="All"){
                        return {
                            status:status,
                            data: await get_logs(status)
                        }
                    }

                })
            )
            setYearStatusCodeLogs(resp);

        }

        else{
            setYearStatusCodeLogs([{
                status:filterStatusCode,
                data: await get_logs(filterStatusCode)
            }])
        }

    };

    const get_status_pie_data = async () => {
        let resp = await fetch("http://127.0.0.1:8000/statusCodeLogs");
        let data = await resp.json();
        setStatusPieData(data);
    };
    // Status code API call ENDS

    useEffect(() => {
        get_statusCodes();
        get_status_pie_data();
    }, []);

    useEffect(() => {
        get_year_statuscode_logs();
    }, [filterStatusCode]);

  return <StatusCodeLogs />;
}

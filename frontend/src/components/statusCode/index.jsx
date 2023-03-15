import React from "react";
import {useState,useContext} from "react";
import {Line,Pie} from "react-chartjs-2"
import Chart from "chart.js/auto";
import { LogsContext } from "../../App";
import { getRandomColor } from "../../utils";
import zoomPlugin from  'chartjs-plugin-zoom';


export default function StatusCodeLogs(){

    Chart.register(zoomPlugin);

    const {
        statusCodes,
        yearStatusCodeLogs,
        statusPieData,
        filterStatusCode,
        setfilterStatusCode
    } = useContext(LogsContext);

    const [hidden,setHidden] = useState(true);

    let datasets = yearStatusCodeLogs.map(status=>{
        if (status!=undefined){
            return {
                label: `${status.status} count`,
                data: status.data,   
                borderWidth: 1,
            }
        }
        return {}
    })


    return(

        <>
            <p className='text-5xl text-center font-bold  mt-10'>Status Code</p>
            
            <div className="flex justify-center item-center mt-7 mb-2">
                <div className="">

                    <div className="dropdown inline-block relative w-full">
                        <button onClick={()=>{setHidden(!hidden)}} className="bg-gray-300 text-gray-700 font-semibold py-2 px-4 rounded inline-flex items-center">
                            <span className="mr-1">{filterStatusCode}</span>
                            <svg className="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/> </svg>
                        </button>
                        <ul className="dropdown-menu absolute text-gray-700 pt-1" hidden={hidden}>
                            {
                            statusCodes.map(type=>(
                                <li className="" onClick={()=>{setfilterStatusCode(type); setHidden(!hidden)}}><a className="rounded-t bg-gray-200 hover:bg-gray-400 py-2 px-4 block whitespace-no-wrap">{type}</a></li>
                            ))
                            }
                        </ul>
                    </div>

                </div>
            </div>

            <div className='w-full flex flex-col'>
                
                <div className='h-[70vh]'>
                    <Line 
                        width={300} 
                        height={500}
                        data={{
                        labels: Array.from({length: 365}, (_, i) => i + 1),
                        datasets: datasets,
                        }}
                        options={{
                            title: { display: true, text: 'Status Code Log Count Chart' },
                            responsive: true,
                            maintainAspectRatio: false,
                            scales:{
                                y:{beginAtZero:false}
                            },
                            plugins: {
                                zoom:{
                                    zoom:{
                                        wheel:{
                                            enabled:true
                                        }
                                    }
                                }
                            }
                            
                        }}
                    />
                </div>
                <div className='h-full mt-20'>
                    <Pie
                        width={300} 
                        height={700}
                        data={{
                        labels: statusPieData.map(item=>item["key"]),
                        datasets: [{
                            data: statusPieData.map(item=>item["doc_count"]),
                            backgroundColor: statusPieData.map(item=>getRandomColor())
                        }]
                        }}
                        options={{
                            responsive: true,
                            maintainAspectRatio: false,
                        }}
                    />
                </div>
            </div>

        </>
    );
}
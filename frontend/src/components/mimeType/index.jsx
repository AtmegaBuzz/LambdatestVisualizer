import React from "react";
import {useState,useContext} from "react";
import {Line,Pie} from "react-chartjs-2"
import Chart from "chart.js/auto";
import { LogsContext } from "../../App";
import { getRandomColor } from "../../utils";

export default function MimeLogs(){

    const {
        mimeTypes,
        yearMimeTypeLogs,
        mimePieData,
        filterMimeType,
        setFilterMimeType,
    } = useContext(LogsContext);

    const [hidden,setHidden] = useState(true);

    

    return(

        <>
            <p className='text-5xl text-center font-bold  mt-20'>Mime Types</p>
            <div className="p-10">

                <div className="dropdown inline-block relative w-1/2 ">
                <button onClick={()=>{setHidden(!hidden)}} className="bg-gray-300 text-gray-700 font-semibold py-2 px-4 rounded inline-flex items-center">
                    <span className="mr-1">{filterMimeType}</span>
                    <svg className="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/> </svg>
                </button>
                <ul className="dropdown-menu absolute text-gray-700 pt-1" hidden={hidden}>
                    {
                    mimeTypes.map(type=>(
                        <li className="" onClick={()=>{setFilterMimeType(type); setHidden(!hidden)}}><a className="rounded-t bg-gray-200 hover:bg-gray-400 py-2 px-4 block whitespace-no-wrap">{type}</a></li>
                    ))
                    }
                </ul>
                </div>

            </div>
            <div className='w-full h-[50vh] flex'>
                
                <div className='w-[50%] h-full'>
                <Line 
                    width={300} 
                    height={700}
                    data={{
                    labels: Array.from({length: 365}, (_, i) => i + 1),
                    datasets: [
                        {
                        label: `${filterMimeType} count`,
                        data: yearMimeTypeLogs,   
                        borderWidth: 1,
                        },
                    ],
                    }}
                    options={{
                    responsive: true,
                    maintainAspectRatio: false,
                    }}
                />
                </div>
            <div className='w-[50%] h-full'>
                <Pie
                width={300} 
                height={700}
                    data={{
                    labels: mimePieData.map(item=>item["key"]),
                    datasets: [{
                        data: mimePieData.map(item=>item["doc_count"]),
                        backgroundColor:[getRandomColor(),getRandomColor(),getRandomColor()]
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
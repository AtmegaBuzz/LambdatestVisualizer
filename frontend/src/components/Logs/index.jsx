import React from "react";
import {useState,useEffect,useContext} from "react";
import {Line,Pie} from "react-chartjs-2"
import Chart from "chart.js/auto";
import { LogsContext } from "../../App";


export default function TotalLogs(){

    const {yearLogCount} = useContext(LogsContext);

    return(

        <>
            <p className='text-5xl text-center font-bold  mt-20'>Log Count</p>

            <div className='w-full h-[50%]'>
            
            <Line 
                width={300} 
                height={700}
                data={{
                labels: Array.from({length: 365}, (_, i) => i + 1),
                datasets: [
                    {
                    label: "Total Log Count",
                    data: yearLogCount,   
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

        </>


    );
}
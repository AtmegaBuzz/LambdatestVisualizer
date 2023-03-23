import { useLocation } from "react-router-dom"
import JSONPretty from 'react-json-pretty';
var JSONPrettyMon = require('react-json-pretty/dist/monikai');


export default function LogDetail(){

    const location = useLocation();
    return (
        <div className="flex w-full h-full p-4 justify-center">
            <JSONPretty className="w-full h-full" theme={JSONPrettyMon} data={location.state.log._source}></JSONPretty>
        </div>
    )    

}
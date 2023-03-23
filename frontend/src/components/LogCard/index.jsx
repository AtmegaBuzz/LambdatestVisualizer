import { useNavigate } from "react-router-dom";

export default function LogCard(props) {

  const navigate = useNavigate();
  let protocol = "null";

  if (props.log._source.params.response.securityDetails!==undefined){
    protocol = props.log._source.params.response.securityDetails.protocol;
  }


  return (
    <div className="overflow-hidden bg-gray-100  shadow-md sm:rounded-lg w-[60%] mt-10">
      <div className="px-4 py-5 sm:px-6">
        <h3 className="text-base font-semibold leading-6 text-gray-900">
          LOGGED ON {props.log._source.datetime}
        </h3>
        <p className="mt-1 max-w-2xl text-md text-gray-500">
          Method: {props.log._source.method}
        </p>
      </div>
      <div className="border-t border-gray-200">
        <dl>
          <div className="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
            <dt className="text-sm font-medium text-gray-500">Mime Tyoe</dt>
            <dd className="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0">
                {props.log._source.params.response.mimeType}
            </dd>
          </div>
          <div className="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
            <dt className="text-sm font-medium text-gray-500">
              Status Code
            </dt>
            <dd className="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0">
                {props.log._source.params.response.status}
            </dd>
          </div>
          <div className="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
            <dt className="text-sm font-medium text-gray-500">Asset URL</dt>
            <dd className="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0">
                {props.log._source.params.response.url}
            </dd>
          </div>
          <div className="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
            <dt className="text-sm font-medium text-gray-500">
                Security State
            </dt>
            <dd className="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0">
                {props.log._source.params.response.securityState}
            </dd>
          </div>
          <div className="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
            <dt className="text-sm font-medium text-gray-500">Protocol</dt>
            <dd className="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0">
              {
                
              }
                {protocol}
            </dd>
          </div>
          <div className="bg-white flex justify-center items-center">
           <button 
            onClick={()=>navigate("/log",{state:{log:props.log}})}
            className="w-[150px] h-[50px] m-5 rounded-md bg-blue-600 text-white font-bold hover:bg-blue-700 ">
                More Info
           </button>
          </div>
          
          
        </dl>
      </div>
    </div>
  );
}

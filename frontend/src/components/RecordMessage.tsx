import { ReactMediaRecorder } from "react-media-recorder";
import RecordIcon from "./RecordIcon";

type Props = {
  handleStop: any;
};

const RecordMessage = ({ handleStop }: Props) => {
  return (
    <ReactMediaRecorder
      audio
      onStop={handleStop}
      render={({ status, startRecording, stopRecording }) => (
        <div className="flex flex-col gap-y-1">
          <div className="h-1/3 flex gap-x-2">
            <span>
              <input className="h-full bg-white p-4 rounded-full"></input>
            </span>
            <span>
              <button
                onMouseDown={startRecording}
                onMouseUp={stopRecording}
                className="h-full bg-white p-1 rounded-full"
              >
                <RecordIcon
                  classText={
                    status == "recording"
                      ? "h-full animate-pulse text-red-500"
                      : "h-full text-sky-500"
                  }
                />
              </button>
              {/* <p className="mt-1 text-white font-light">{status}</p> */}
            </span>
          </div>
          <p className="w-full mt-1 text-white font-light">{status}</p>
        </div>
      )}
    />
  );
};

export default RecordMessage;

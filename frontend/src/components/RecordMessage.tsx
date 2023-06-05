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
        <div className="mt-2">
          <span>
            <input className="bg-white p-4 rounded-full"></input>
          </span>
          <span>
            <button
              onMouseDown={startRecording}
              onMouseUp={stopRecording}
              className="bg-white p-1 rounded-full"
            >
              <RecordIcon
                classText={
                  status == "recording"
                    ? "animate-pulse text-red-500"
                    : "text-sky-500"
                }
              />
            </button>
            <p className="mt-2 text-white font-light">{status}</p>
          </span>
        </div>
      )}
    />
  );
};

export default RecordMessage;

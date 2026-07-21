import { useState } from "react";

function UploadDocuments() {
    const [files, setFiles] = useState([]);
    const [message, setMessage] = useState("");

    function handleFileChange(event) {
        setFiles(event.target.files);
    }

    async function uploadDocuments() {
        const formData = new FormData();

        for (let i = 0; i < files.length; i++) {
            formData.append(
                "files",
                files[i]
            );
        }

        const response = await fetch(
            "http://127.0.0.1:8000/upload",
            {
                method: "POST",
                body: formData
            }
        );

        const data = await response.json();

        setMessage(data.message);
    }

    return (
        <div>

            <h2>
                Upload Documents
            </h2>

            <input
                type="file"
                multiple
                accept=".pdf"
                onChange={handleFileChange}
            />

            <button onClick={uploadDocuments}>
                Upload
            </button>

            <p>
                {message}
            </p>

        </div>
    );
}


export default UploadDocuments;
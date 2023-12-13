import CIcon from '@coreui/icons-react';
import React, {ChangeEvent, useState } from 'react';
import axios from 'axios';
import { cilList, cilSave } from '@coreui/icons';
import {
    CButton,
    CCard,
    CCardBody,
    CCardHeader,
    CCol,
    CForm,
    CFormInput,
    CFormLabel,
    CRow,
  } from '@coreui/react'
import { API_BASE_URL } from 'src/appConfig';
  
  const FileUpload = () => {
    const [files, setFileList] = useState<FileList | null>(null);
    
  
    const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
        setFileList(e.target.files);
      };
      
    const handleUpload = async (e:any) => {
        if (!files) {
            return;
          }
        try {
            // const formData = new FormData();
            const data= new FormData();
            const config = {
              headers: {
                "content-type": "multipart/form-data",
                Authorization: localStorage.getItem("token"),
              },
            }
        
          for(let i=0;i<files.length;i++)
          {
            
            if(files[i].type=="video/mp4"){
              data.append('video_file', files[i],files[i].name); 
            }
            else if(files[i].type=="text/csv"){
              data.append('csv_file', files[1],files[1].name); 
            }
            else{
              alert("only mp4 and csv support"); 
              return
            }
          
          //   //data.append('files', files[i],files[i].name); 
          //   if(i==0)
          //   // data.append('video_file', files[0],files[0].name); 
          // else
          // // data.append('csv_file', files[1],files[1].name); 
          }
          const url="upload-data/";
          const response=axios.post(`${API_BASE_URL}${url}`, data, config).then(response => {
              console.log(response.data)
            });
            console.log(response);
            alert('Files uploaded successfully!');
        } 
        catch (error) {
           console.error('Error uploading files:', error);
         }
       };

    return (
      <CRow>
        <CCol xs={12}>
          <CCard className="mb-4">
            <CCardHeader>
              <strong>Upload</strong>
            </CCardHeader>
            <CCardBody>
                <CForm onSubmit={handleUpload}>
                    <CRow>
                    <div className="mb-3">
                        <CFormLabel  className="form-label">Multiple files input example</CFormLabel>
                        <CFormInput className="form-control" type="file" id="formFileMultiple" multiple onChange={handleFileChange}/>
                    </div>
                    </CRow>
                    <CRow>
                <CCol xs={12} sm={12} className="mb-3">
                  <div className="d-grid gap-2 d-md-flex justify-content-md-end">
                    <CButton color="success" shape="rounded-pill" className="me-md-2" type="submit">
                    &nbsp;<CIcon icon={cilSave} />&nbsp;Save&nbsp;</CButton>
                  </div>
                </CCol>
              </CRow>
                </CForm>
            </CCardBody>
          </CCard>
        </CCol>
      </CRow>      
    )
  }
  
  export default FileUpload
  
import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import {
    CCard,
    CCardBody,
    CCardHeader,CImage,
    CCol,
    CRow,
    CFormLabel,
  } from '@coreui/react'
import { API_BASE_URL, SERVER_STATIC_FILE_URL } from 'src/appConfig';

  const FileDownload = () => {
     const baseUrl = SERVER_STATIC_FILE_URL;
    const[videoUrl,setVideoUrl]=useState('');
    const [imageUrl1, setImageUrl1] = useState('');
    const [imageUrl2, setImageUrl2] = useState('');
    const [imageUrl3, setImageUrl3] = useState('');
    // const [files, setFiles] = useState<string[]>([]);
    const [showVideo, setShowVideo] = useState(false);
    useEffect(() => {
      const fetchImgFiles = async () => {
        try {
            const url="download-data/"
            const response = await fetch(`${API_BASE_URL}${url}`);
            
            const data=await response.json();
            console.log(data);
            
            setVideoUrl(data.videoFile);
            setImageUrl1(data.images[0]);
            setImageUrl2(data.images[1]);
            setImageUrl3(data.images[2]);
            setShowVideo(true);
        } catch (error) {
            console.error('Error fetching file list:', error);
        }
    };

    fetchImgFiles();
    }, []);

    return (
      <CRow>
        <CCol xs={12}>
          <CCard className="mb-4">
            <CCardHeader>
              <strong>Video/ Chart View</strong>
            </CCardHeader>
            <CCardBody>              
                <CRow>
                  <CCol>   
                      {showVideo && (         
                        <video id="vdo" width="640" height="360" controls autoPlay loop muted>
                        <source src={videoUrl} type="video/mp4" />
                        
                      </video>
                      )}
                  </CCol>
                </CRow>
            </CCardBody>
            <CCardBody>
                <CRow>
                  <CCol>
                    <CImage fluid src={imageUrl1} width={200} height={200} />
                  </CCol>
                  <CCol>
                    <CImage fluid src={imageUrl2} width={200} height={200} />
                  </CCol>
                  <CCol>
                    <CImage fluid src={imageUrl3} width={200} height={200} />
                  </CCol>
                </CRow>                
            </CCardBody>
          </CCard>
        </CCol>
      </CRow>      
    )
  }
  
  export default FileDownload
  
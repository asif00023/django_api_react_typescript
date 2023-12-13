
import {
  CCard,
  CCardBody,
  CCardHeader,
  CCol,
  CRow,
} from '@coreui/react'




const Dashboard = () => {
  return (
    <CRow>
      <CCol xs={12}>
        <CCard className="mb-4">
          <CCardHeader>
            <strong>Landing Page/Dashboard</strong>
          </CCardHeader>
          <CCardBody>
            <div className="d-grid gap-2 col-6 mx-auto">
            <CRow>
              <strong>Company Name: Vision-Surgery</strong>
            </CRow>
            <CRow>
              Candidate Name: Asif Mahamud
            </CRow><CRow>
              Email: asif.kucse@gmail.com
            </CRow><CRow>
              Mobile: +4917616743289
            </CRow><CRow>  
              <strong>Assignment Description</strong>
            </CRow><CRow>  
            <a href='https://github.com/jingvsai/Coding-Test-React-Django/tree/main/python_script' target='_blank'>Assignment Requirement Description</a>
            </CRow>
            </div>
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>      
  )
}

export default Dashboard

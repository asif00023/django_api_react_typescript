import React from 'react'
import { CFooter } from '@coreui/react'

const AppFooter = () => {
  return (
    <CFooter>
      {/* <div>
        <a href="https://coreui.io" target="_blank" rel="noopener noreferrer">
          CoreUI
        </a>
        <span className="ms-1">&copy; 2023 creativeLabs.</span>
      </div> */}
      <div className="ms-auto">
        <span className="me-1">Developed by</span>
        <a href="https://www.linkedin.com/in/asifmahamud-7278226b/" target="_blank" rel="noopener noreferrer">
          An assignment with react typescript & python -- Asif Mahamud
        </a>
      </div>
    </CFooter>
  )
}

export default React.memo(AppFooter)

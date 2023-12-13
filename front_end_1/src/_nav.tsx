import React from 'react'
import CIcon from '@coreui/icons-react'
import {
  cilBell,
  cilCalculator,cilLibraryAdd,cilLibrary,cilLibraryBuilding,
  cilChartPie,
  cilCursor,
  cilDescription,
  cilDrop,
  cilNotes,
  cilPencil,
  cilPuzzle,
  cilSpeedometer,
  cilStar,
  cilLayers,
} from '@coreui/icons'
import { CNavGroup, CNavItem, CNavTitle } from '@coreui/react'

const _nav = [    
  {
    component: CNavGroup,
    name: 'Files',
    to: '/files',
    // icon: <CIcon icon={cilCursor} customClassName="nav-icon" />,
    icon: <CIcon icon={cilLayers} customClassName="nav-icon" />,
    items: [
      {
        component: CNavItem,
        name: 'Upload',
        icon: <CIcon icon={cilLibraryAdd} customClassName="nav-icon" />,
        to: '/files/upload',
      },
      {
        component: CNavItem,
        name: 'Download',
        icon: <CIcon icon={cilLibrary} customClassName="nav-icon" />,
        to: '/files/download',
      },
    ],
  }
  // {
  //   component: CNavItem,
  //   name: 'Docs',
  //   href: 'https://coreui.io/react/docs/templates/installation/',
  //   icon: <CIcon icon={cilDescription} customClassName="nav-icon" />,
  // },
]

export default _nav

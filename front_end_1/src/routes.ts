import React from 'react'

const Dashboard = React.lazy(() => import('./app/views/dashboard/Dashboard'))




const FileUpload = React.lazy(() => import('./app/views/files/upload/upload'))
const FileDownload = React.lazy(() => import('./app/views/files/download/download'))


const routes = [
  { path: '/', exact: true, name: 'Home' },
  { path: '/dashboard', name: 'Dashboard', element: Dashboard },

  // { path: '/materials', name: 'Materials', element: MaterialsList, exact: true },
  // { path: '/materials/create', name: 'Create', element: MaterialsCreate },
  // { path: '/materials/details', name: 'Details', element: MaterialsDetails },
  // { path: '/materials/list', name: 'List', element: MaterialsList },
  // { path: '/materials/edit', name: 'List', element: MaterialsEdit },

  { path: '/files', name: 'Files', element: FileDownload, exact: true },
  { path: '/files/upload', name: 'Upload', element: FileUpload },
  { path: '/files/download', name: 'Download', element: FileDownload },
  

]

export default routes

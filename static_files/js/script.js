//THIS CHANGES THE REPORT STATE
let updateTOApproved = document.getElementsByClassName('Approved')
let updateTODeclined = document.getElementsByClassName('Declined')

for(var i=0; i< updateTOApproved.length; i++){
    updateTOApproved[i].addEventListener('click', function(){
        var leaveId= this.dataset.leave
        var action = this.dataset.action
        // console.log('reportid', reportId, 'action', action)
        // console.log('USER:', user)
        if(user==='AnonymousUser'){
          console.log('Not Logged in')
        }else{
          updateStatus(leaveId,action)
        }
    })
}

for(var i=0; i< updateTODeclined.length; i++){
  updateTODeclined[i].addEventListener('click', function(){
      var leaveId= this.dataset.leave
      var action = this.dataset.action
      // console.log('reportid', reportId, 'action', action)
      // console.log('USER:', user)
      if(user==='AnonymousUser'){
        console.log('Not Logged in')
      }else{
        updateStatus(leaveId,action)
      }
  })
}

function updateStatus(leaveId, action){
  console.log('user is logged in, sending data')
  var url = '/update_leave/'
  fetch(url, {
    method:'POST',
    headers:{
      'Content-Type':'application/json',
      'X-CSRFToken':csrftoken,
    },
    body:JSON.stringify({
      'leaveId':leaveId, 'action':action,
    })
  })
  .then((response)=>{
    return response.json()
  })
  .then((data)=>{
    console.log('data:', data)
   location.reload()
   
  })
  
}
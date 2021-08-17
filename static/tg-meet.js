var apiObj = null;

function StartMeeting(roomName,dispName){
    const domain = 'meet.jit.si';
    const options = {
        roomName: roomName,
        width: 1080,
        height: 720,
        parentNode: document.querySelector('#jitsi-meet-conf-container'),
        userInfo: {
            displayName: dispName
        },
        configOverwrite: {
            startWithAudioMuted: true,
            enableClosePage: false
        },
        // interfaceConfigOverwrite: {
        //     DEFAULT_LOGO_URL: '',
        //     DEFAULT_WELCOME_PAGE_LOGO_URL: 'www.google.com',
        //     JITSI_WATERMARK_LINK: 'www.google.com',
        //     SHOW_BRAND_WATERMARK: false,
        //     SHOW_JITSI_WATERMARK: false,
        //     SHOW_WATERMARK_FOR_GUESTS: false,
        // },
        onload: function() {
            $('#inpForm').hide();
            $('#endMsg').hide();
        }
    };
    apiObj = new JitsiMeetExternalAPI(domain, options);

    apiObj.addEventListeners({
        readyToClose: function() {
            var div = document.getElementById('jitsi-meet-conf-container');
            while(div.firstChild){
                div.removeChild(div.firstChild);
            }
            // $('#jitsi-meet-conf-container').empty();
            // $('#jitsi-meet-conf-container').hide();
            $('#inpForm').show();
            $('#endMsg').show().text('Your meeting has ended. You can start another one.');

        }
    });

    apiObj.executeCommand('subject', roomName);
}

function HangupCall(){
    apiObj.executeCommand('hangup');
}

// function StartMeeting() {
//     const domain = 'meet.jit.si';
//     const options = {
//         roomName: 'TestRoom',
//         width: 720,
//         height: 640,
//         parentNode: document.querySelector('#jitsi-meet-conf-container')
//     };
//     apiObj = new JitsiMeetExternalAPI(domain, options);
// }

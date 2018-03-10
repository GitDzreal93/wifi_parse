/**
 * 微信连Wi-Fi协议3.1供运营商portal呼起微信浏览器使用
 */
 var loadIframe = null;
 var noResponse = null;

 var errorJump = function() {
    alert('对不起，您的浏览器无法打开微信');
 };
 function createIframe(){
	 var iframe = document.createElement("iframe");
     iframe.style.cssText = "display:none;width:0px;height:0px;";
     document.body.appendChild(iframe);
     loadIframe = iframe;
 }
//注册回调函数
function jsonpCallback(result){  
	if(result && result.success){
		var ua=navigator.userAgent;              
		if (ua.indexOf("iPhone") != -1 ||ua.indexOf("iPod")!=-1||ua.indexOf("iPad") != -1) {   //iPhone             
			document.location = result.data;
		}else{
		    createIframe();
		    loadIframe.src=result.data;
            if (wxmode == 0) {
			alert("由于微信控制等原因，点击“确定”后，如果手机收到广告，说明当前测试公众号可正常工作，可以使用盒子强推功能；如果测试手机没有收到推送，说明当前测试公众号不能正常工作，请稍后再试，一般一个公众号被限制的时间为24小时！");
            } else {
                wxsucc++;
                $('#wxsucc').html('共成功推送: ' + wxsucc);
                var v = $('#detail').val();
                $('#detail').val(v + "\t成功\n");
            }
			//alert(result.data);
            /*
			noResponse = setTimeout(function(){
				errorJump();
	      	},120000);
            */
		}
	}else if(result && !result.success){
        if (wxmode == 0) {
            var re = /[Ff][Rr][Ee][Qq]/;
            if (re.test(result.data)) {
                alert('公众号调用过于频繁，请稍后再试');
                return;
            }
            re = /[Bb][Ll][Aa][Cc][Kk]/;
            if (re.test(result.data)) {
                alert('公众号进入黑名单');
                return;
            }

            alert(result.data);
        } else {
            var v = $('#detail').val();
            $('#detail').val(v + "\t失败\n");
        }
	}
}

function Wechat_GotoRedirect(appId, extend, timestamp, sign, shopId, authUrl, mac, ssid, bssid){
	
	//将回调函数名称带到服务器端
	var url = "https://wifi.weixin.qq.com/operator/callWechatBrowser.xhtml?appId=" + appId 
																		+ "&extend=" + extend 
																		+ "&timestamp=" + timestamp 
																		+ "&sign=" + sign;	
	
	//如果sign后面的参数有值，则是新3.1发起的流程
	if(authUrl && shopId){
		
		
		url = "https://wifi.weixin.qq.com/operator/callWechat.xhtml?appId=" + appId 
																		+ "&extend=" + extend 
																		+ "&timestamp=" + timestamp 
																		+ "&sign=" + sign
																		+ "&shopId=" + shopId
																		+ "&authUrl=" + encodeURIComponent(authUrl)
																		+ "&mac=" + mac
																		+ "&ssid=" + ssid
																		+ "&bssid=" + bssid;
		
	}			
	
	//通过dom操作创建script节点实现异步请求  
	var script = document.createElement('script');  
	script.setAttribute('src', url);  
	document.getElementsByTagName('head')[0].appendChild(script);
}

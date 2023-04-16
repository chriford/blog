const deleteBlog = (pk, title, status) => {
    const is_confirmed = confirm(`DELETE BLOG '${title}'`);
    if (is_confirmed) {
        const deleteblog = document.getElementById('deleteblog');
        deleteblog.href = `/blog/${title}/status/${status}/blog/${pk}/`
        deleteblog.onclick = ""
        deleteblog.click()
    }
}
const deactivateBlog = (pk, title, status) => {
    const is_confirmed = confirm(`DEACTIVATE BLOG '${title}'`);
    if(is_confirmed){
        const deactivateblog = document.getElementById('deactivateblog');
        deactivateblog.href = `/blog/${title}/status/${status}/blog/${pk}/`
        deactivateblog.onclick = ""
        deactivateblog.click()
    }
} 
const reactivateBlog = (pk, title, status) => {
    const is_confirmed = confirm(`REACTIVATE BLOG '${title}'`);
    if(is_confirmed){
        const deactivateblog = document.getElementById('reactivateblog');
        deactivateblog.href = `/blog/${title}/status/${status}/blog/${pk}/`
        deactivateblog.onclick = ""
        deactivateblog.click()
    }
}
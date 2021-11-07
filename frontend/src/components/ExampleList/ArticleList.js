import React from "react";

const ArticleList = (props) => {

    return (
        <div>
        {/* Display the article details if article is not None */} 
   	    {props.articles && props.articles.map(article =>{
            return (
              <div key= {article.id} className="my-2">
                <h2 className="text-primary"> {article.title} </h2>
                <p> { article.body } </p>
                <p> { article.date } </p>
    	          <hr/>
              </div>
            )
            
            })}
        </div>
        )
}

export default ArticleList;
Measuring YouTube Content Delivery over IPv6  
[ACM SIGCOMM Computer Communication Review &rarr;](http://www.sigcomm.org/publications/computer-communication-review)  
XXX 2017 (to appear)  

---  

### Test

The `youtube` test used to collect the dataset is available [here
&rarr;](https://github.com/sabyahsan/Youtube-test)  

### Vantage Points

The dataset is collected from ~100 SamKnows probes:

![](http://i.imgur.com/zVefNfd.png)  

### Dataset

The raw dataset and mirrors are available at:

* Jacobs University Bremen, [here
  &rarr;](http://cnds.eecs.jacobs-university.de/users/vbajpai/yt-ccr-2017/)  

It includes the SQL schema `youtube.sql` and the dataset in sqlite3
format `youtube.db` and the metadata associated with each vantage point.

### Installation

`make` will install the python dependencies required to run the jupyter
notebooks. `make run` will run jupyter.


### Repeating the results

`plot-*` notebooks can be used to repeat the analysis on the existing
dataset. Each such notebook produces a single plot in the paper.


### Contact

Please feel welcome to contact the authors for further details.

- Vaibhav Bajpai <bajpaiv@in.tum.de>  
- Saba Ahsan <saba.ahsan@aalto.fi>>  
- Jürgen Schönwälder <j.schoenwaelder@jacobs-university.de>  
- Jörg Ott <ott@in.tum.de>





# <div align="center">![output-onlinepngtools.png](rpio%2Fassets%2Foutput-onlinepngtools.png)      robosapiensIO       ![output-onlinepngtools.png](rpio%2Fassets%2Foutput-onlinepngtools.png)</div>

---

# <div align="center">![](rpio%2Fassets%2FroboSAPIENS_banner_space_theme.png)</div>

This repository provides a flexible software architecture framework for building self-adaptive, trustworthy robotic applications using the RoboSapiens Adaptive Platform. It includes modular building blocks for runtime adaptation, trustworthiness monitoring, and knowledge management, enabling the seamless deployment of adaptive systems in diverse environments. The platform supports both resource-constrained and high-performance computing setups, facilitating reliable, automated responses to changing operational conditions. 


## <div align="center">RPIO 🚀 NEW</div>

---


    

## <div align="center">RPIO releases</div>

---
In the table below, the features of the rpio framework are specified:

| Level               | Group                       |         Feature         | Pre-release | v0.1 |
|---------------------|-----------------------------|:-----------------------:|:-----------:|:----:|
| **Architecture**    | **Knowledge manager**       |       _r/w data_        |      ✔      |      |
|                     |                             |       _r/w event_       |      ✔      |      |
|                     |                             |  _r/w historical data_  |      ❌      |      |
|                     |                             |      _persistency_      |      ✔      |      |
|                     | **Communcation manager**    |      MQTT support       |      ✔      |      |
|                     |                             |      Redis support      |      ✔      |      |
|                     |                             |    RabbitMQ support     |      ❌      |      |
|                     |                             |     Modbus support      |      ❌      |      |
|                     | **Trustworthiness manager** |                         |      ❌      |      |
|                     |                             |                         |             |      |
|                     | **Trustworthiness checker** | component ET monitoring |      ✔      |      |
|                     |                             |       stl support       |      ❌      |      |
| **rpio**            | **Transformations**         |      _aadl2aadlIl_      |      ❌      |      | 
|                     |                             |       _aadl2swc_        |      ✔      |      |
|                     |                             |     _aadl2message_      |      ✔      |      |
|                     |                             |      upload image       |      ❌      |      |
|                     | **PyLauncher**              |   launch  python swc    |      ✔      |      |
|                     | **Command line interface**  |  _run transformations_  |     🤔      |      |
|                     |                             |       _run code_        |     🤔      |      |
|                     |                             |      _deploy code_      |     🤔      |      |
|                     | **Remote agent**            |       remote cmds       |     🤔      |      |
|                     |                             |       remote ping       |     🤔      |      |
|                     |                             |           OTA           |     🤔      |      |
|                     | **Remote manager**          |   remote device cmds    |      🤔       |      |
|                     |                             |   remote device ping    |       🤔      |      |
|                     |                             |    remote device OTA    |       🤔      |      |
| **ClientLibraries** | **rpclpy**                  |       _r/w data_        |      ✔      |      |
|                     |                             |       _r/w event_       |      ✔      |      |
|                     |                             |  _r/w historical data_  |      ✔      |      |
|                     |                             |     _signal status_     |      ❌      |      |

### Release descriptions

**Pre-release:**
- Initial version of the rpio framework
- Initial version of the client library for python (rpclpy)
    

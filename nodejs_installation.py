import os, time, sys

if len(sys.argv) < 1:
    print("Error, Missing argument\nUsage: python " + sys.argv[0] + " <1/2>\r\n")
else: 
    part = sys.argv[1]
    if part == "1" or part == 1:
        os.system("yum -y update -q")
        os.system('yum -y groupinstall "Development Tools" -q')
        os.system("yum -y install screen")
        os.system("cd /usr/src")
        time.sleep(5)
        os.system("wget http://nodejs.org/dist/v0.10.4/node-v0.10.4.tar.gz")
        os.system("tar zxf node-v0.10.4.tar.gz")
        os.system("cd node-v0.10.4")
        os.system("./configure")
        os.system("make")
        os.system("make install")
        os.system("yum install -y gcc-c++ make")
        os.system("sudo npm update npm -g")
        os.system("sudo yum purge nodejs npm")
        os.system("curl -sL https://rpm.nodesource.com/setup_10.x | sudo bash -")
        os.system("sudo yum install -y nodejs")
        os.system("npm config set registry http://registry.npmjs.org/")
        os.system("curl https://raw.githubusercontent.com/creationix/nvm/v0.30.2/install.sh | bash")
        os.system("curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash")
        os.system("npm config set strict-ssl false")
        os.system("npm config set strict-ssl false")
        print("First part is finished. restart you're terminal and run part 2\r\nUsage: python " + sys.argv[0] + " 2\r\n")
    elif part == "2" or part == 2:
        os.system("nvm install 10.15.3")
        print("NODEJS and NPM is fully installed!\r\nEnjoy\r\n")

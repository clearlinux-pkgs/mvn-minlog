#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-minlog
Version  : 1.3.0
Release  : 2
URL      : https://github.com/EsotericSoftware/minlog/archive/minlog-1.3.0.tar.gz
Source0  : https://github.com/EsotericSoftware/minlog/archive/minlog-1.3.0.tar.gz
Source1  : https://repo1.maven.org/maven2/com/esotericsoftware/minlog/1.3.0/minlog-1.3.0.jar
Source2  : https://repo1.maven.org/maven2/com/esotericsoftware/minlog/1.3.0/minlog-1.3.0.pom
Source3  : https://repo1.maven.org/maven2/com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.jar
Source4  : https://repo1.maven.org/maven2/com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: mvn-minlog-data = %{version}-%{release}
Requires: mvn-minlog-license = %{version}-%{release}

%description
![](https://raw.github.com/wiki/EsotericSoftware/minlog/images/logo.png)
## MinLog

%package data
Summary: data components for the mvn-minlog package.
Group: Data

%description data
data components for the mvn-minlog package.


%package license
Summary: license components for the mvn-minlog package.
Group: Default

%description license
license components for the mvn-minlog package.


%prep
%setup -q -n minlog-minlog-1.3.0

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-minlog
cp license.txt %{buildroot}/usr/share/package-licenses/mvn-minlog/license.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/esotericsoftware/minlog/1.3.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/esotericsoftware/minlog/1.3.0/minlog-1.3.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/esotericsoftware/minlog/1.3.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/esotericsoftware/minlog/1.3.0/minlog-1.3.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/esotericsoftware/minlog/minlog/1.2
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/esotericsoftware/minlog/minlog/1.2
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/esotericsoftware/minlog/1.3.0/minlog-1.3.0.jar
/usr/share/java/.m2/repository/com/esotericsoftware/minlog/1.3.0/minlog-1.3.0.pom
/usr/share/java/.m2/repository/com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.jar
/usr/share/java/.m2/repository/com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-minlog/license.txt

Summary: The basic required files for the root user's directory
Name: rootfiles
Version: 8.1
Release: 1
License: Public Domain
Group: System Environment/Base

Source0: %{name}-%{version}.tar.bz2
Source1: dot-bashrc
Source2: dot-bash_profile
Source3: dot-bash_logout
Source4: dot-tcshrc
Source5: dot-cshrc

BuildArch: noarch

%description
The rootfiles package contains basic required files that are placed
in the root user's account.  These files are basically the same
as those in /etc/skel, which are placed in regular
users' home directories.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/root

for file in %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} ; do
  f=`basename $file`
  install -p -m 644 $file $RPM_BUILD_ROOT/root/${f/dot-/.}
done

## Currently we have older cp that doesn't support -n option thus commenting this out for now
#%posttrans
#if [ $1 -eq 0 ] ; then
#  #copy recursively the content, but do not overwrite the original files provided by rootfiles package
#  cp -ndr --preserve=ownership,timestamps /etc/skel/. /root/ || :
#fi

%files
%defattr(-,root,root,-)
%config(noreplace) /root/.[A-Za-z]*


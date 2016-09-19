Name:           deskos-indexhtml
Summary:        Browser default start page for DeskOS
Version:        7
Release:        0.1.0%{?dist}

License:        GPLv3+
Group:          Documentation
BuildArch:      noarch
Obsoletes:      indexhtml <= 2:5-1
Obsoletes:      redhat-indexhtml
Provides:       redhat-indexhtml
Obsoletes:      centos-indexhtml
Provides:       centos-indexhtml

Source0:        index.html
Source1:        deskos-logo.png
Source2:        background.png

%description
The indexhtml package contains the welcome page shown by your Web browser,
which you'll see after you've successfully installed DeskOS Linux

%install
mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML
mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML/es

cp -a %SOURCE0 %SOURCE1 %SOURCE2 $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML/

pushd $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML/es
ln -s ../index.html .
ln -s ../deskos-logo.png .
ln -s ../background.png .
popd

%files
%defattr(-,root,root,-)
%{_defaultdocdir}/HTML/*

%changelog
* Sun Sep 18 2016 Ricardo Arguello <rarguello@deskosproject.org> - 7-0.1.0
- Initial DeskOS branding

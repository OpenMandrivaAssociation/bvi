Name: bvi
Version: 1.3.2
Release: %mkrel 2
Summary: A vi-like binary file editor
URL: http://bvi.sourceforge.net/
Source: bvi-%{version}.tar.bz2
Patch: bvi-1.3.2-config.guess.patch.bz2
Group: Editors
License: GPL
BuildRequires: libncurses-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
bvi is a display-oriented editor for binary files, based on the vi
text editor. If you are familiar with vi, just start the editor and
begin to edit! If you never heard about vi, maybe bvi is not the
best choice for you.

%prep
%setup -q
%patch0 -p1

%build
%configure --libdir=%{_datadir}
make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_libdir}

install -s -m 755 bvi %{buildroot}%{_bindir}/bvi
install -s -m 755 bmore %{buildroot}%{_bindir}/bmore
install -m 644 bvi.1 %{buildroot}%{_mandir}/man1/bvi.1
install -m 644 bmore.1 %{buildroot}%{_mandir}/man1/bmore.1
install -m 644 bmore.help %{buildroot}%{_datadir}/bmore.help
ln -sf bvi %{buildroot}%{_bindir}/bview
ln -sf bvi %{buildroot}%{_bindir}/bvedit
echo ".so man1/bvi.1" > %{buildroot}%{_mandir}/man1/bview.1
echo ".so man1/bvi.1" > %{buildroot}%{_mandir}/man1/bvedit.1
chmod 644 README COPYING CHANGES CREDITS

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING CHANGES CREDITS
%{_bindir}/bvi
%{_bindir}/bmore
%{_bindir}/bview
%{_bindir}/bvedit
%{_mandir}/man1/bvi.1*
%{_mandir}/man1/bmore.1*
%{_mandir}/man1/bview.1*
%{_mandir}/man1/bvedit.1*
%{_datadir}/bmore.help


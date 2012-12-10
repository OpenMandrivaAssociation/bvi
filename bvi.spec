Name: bvi
Version: 1.3.2
Release: 7
Summary: A vi-like binary file editor
URL: http://bvi.sourceforge.net/
Source: bvi-%{version}.tar.bz2
Patch0: bvi-1.3.2-config.guess.patch.bz2
Patch1: bvi-1.3.2-mdv-fix-str-fmt.patch
Group: Editors
License: GPLv2+
BuildRequires: pkgconfig(ncurses)

%description
bvi is a display-oriented editor for binary files, based on the vi
text editor. If you are familiar with vi, just start the editor and
begin to edit! If you never heard about vi, maybe bvi is not the
best choice for you.

%prep
%setup -q
%patch0 -p1
%patch1 -p1 -b .strfmt

%build
%configure --libdir=%{_datadir}
make

%install
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



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.2-6mdv2011.0
+ Revision: 610087
- rebuild

* Sat Dec 12 2009 Jérôme Brenier <incubusss@mandriva.org> 1.3.2-5mdv2010.1
+ Revision: 477740
- fix str fmt
- fix license tag

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.3.2-4mdv2009.0
+ Revision: 243376
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.3.2-2mdv2008.1
+ Revision: 140691
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import bvi


* Tue Aug 01 2006 Lenny Cartier <lenny@mandriva.com> 1.3.2-2mdv2007.0
- rebuild

* Fri May  6 2005 Claudio Matsuoka <claudio@mandriva.com> 1.3.2-1mdk
- package creation

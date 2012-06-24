Summary:	GNU Octave -- a high-level language for numerical computations
Summary(es):	GNU Octave - Un programa para c�lculo num�rico y matricial
Summary(pl):	GNU Octave -- j�zyk programowania do oblicze� numerycznych
Summary(pt_BR):	GNU Octave - Um programa para c�lculo num�rico e matricial
Name:		octave
Version:	2.1.36
Release:	9
License:	GPL
Group:		Applications/Math
Source0:	ftp://ftp.che.wisc.edu/pub/octave/bleeding-edge/%{name}-%{version}.tar.bz2
Patch0:		%{name}-lib%{name}.info.patch
Patch1:		%{name}-Octave-FAQ.info.patch
Patch2:		%{name}-DESTDIR.patch
URL:		http://www.che.wisc.edu/octave/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gcc-g77
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel
Requires:	gnuplot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Octave is a high-level language, primarily intended for numerical
computations. It provides a convenient command line interface for
solving linear and nonlinear problems numerically, and for performing
other numerical experiments using a language that is mostly compatible
with Matlab. It may also be used as a batch-oriented language.

Octave has extensive tools for solving common numerical linear algebra
problems, finding the roots of nonlinear equations, integrating
ordinary functions, manipulating polynomials, and integrating ordinary
differential and differential-algebraic equations. It is easily
extensible and customizable via user-defined functions written in
Octave's own language, or using dynamically loaded modules written in
C++, C, Fortran, or other languages.

%description -l es
GNU Octave - Un programa de c�lculo num�rico y matricial. Posee
lenguaje de altonivel y ambiente interactivo para computaci�n
num�rica, semejantes a los del Matlab.

%description -l pl
GNU Octave jest j�zykiem programowania wysokiego poziomu przeznaczonym
g��wnie do oblicze� numerycznych. Octave jest w du�ym stopniu
kompatybilny z j�zykiem Matlab. Pracowa� mo�na wprost z linii polece�
lub uruchamia� programy stworzone za pomoc� zewn�trznego edytora.

%description -l pt_BR
GNU Octave - Um programa de c�lculo num�rico e matricial. Possui
linguagem de alto n�vel e ambiente interativo para computa��o num�rica
semelhantes ao do Matlab.

%package devel
Summary:	Header files and devel docs for Octave
Summary(pl):	Pliki nag��wkowe i dodatkowa dokumentacja Octave
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and devel docs for Octave.

%description devel -l pl
Pliki nag��wkowe i dodatkowa dokumentacja Octave.

%package -n xemacs-octave-mode-pkg
Summary:	XEmacs mode for Octave
Summary(pl):	Tryb edycji plik�w Octave dla XEmacsa
Group:		Applications/Editors/Emacs
Requires:	xemacs

%description -n xemacs-octave-mode-pkg
XEmacs mode for Octave.

%description -n xemacs-octave-mode-pkg -l pl
Tryb edycji plik�w Octave dla XEmacsa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
#aclocal
#autoconf
cp -f %{_datadir}/automake/config.* .
%configure2_13 \
	--with-g77 \
	--enable-dl \
	--enable-shared \
	--enable-rpath \
	--enable-lite-kernel

%{__make}
%{__make} -C doc/faq Octave-FAQ.info
%{__make} -C doc/liboctave liboctave.info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	octincludedir=$RPM_BUILD_ROOT%{_includedir}

ln -sf %{_includedir}/%{name} $RPM_BUILD_ROOT%{_includedir}/%{name}-%{version}

install doc/liboctave/*.info* $RPM_BUILD_ROOT%{_infodir}
install doc/faq/*.info* $RPM_BUILD_ROOT%{_infodir}

## xemacs-octave-mode-pkg
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/octave-mode
cp -a emacs/*.el $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/octave-mode
# add otags script or not (additional Requires: ctags)???
#cp -a emacs/otags $RPM_BUILD_ROOT%{_bindir}
cat <<EOF >$RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/octave-mode/auto-autoloads.el
(autoload 'run-octave "octave-inf" nil t)
(autoload 'octave-help "octave-hlp" nil t)
(autoload 'octave-mode "octave-mod" nil t)
(setq auto-mode-alist
      (cons '("\\\\.m$" . octave-mode) auto-mode-alist))
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS THANKS PROJECTS
%doc emacs examples doc/{interpreter,faq}/*.html
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%{_infodir}/octave.info*
%{_infodir}/Octave-FAQ.info*
%{_mandir}/man1/*
%{_datadir}/octave

%files devel
%defattr(644,root,root,755)
%doc doc/refcard/refcard{-a4,}.* doc/liboctave/*.html
%{_includedir}/%{name}*
%{_infodir}/liboctave.info*

%files -n xemacs-octave-mode-pkg
%defattr(644,root,root,755)
%{_datadir}/xemacs-packages/lisp/*

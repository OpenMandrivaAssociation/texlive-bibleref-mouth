# revision 25527
# category Package
# catalog-ctan /macros/latex/contrib/bibleref-mouth
# catalog-date 2012-02-27 12:45:12 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-bibleref-mouth
Version:	1.0
Release:	1
Summary:	Consistent formatting of Bible references
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bibleref-mouth
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-mouth.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-mouth.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-mouth.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows Bible references to be formatted in a
consistent way. It is similar to the bibleref package, except
that the formatting macros are all purely expandable -- that
is, they are all implemented in TeX's mouth. This means that
they can be used in any expandable context, such as an argument
to a \url command.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bibleref-mouth/bibleref-mouth.sty
%doc %{_texmfdistdir}/doc/latex/bibleref-mouth/README
%doc %{_texmfdistdir}/doc/latex/bibleref-mouth/bibleref-mouth.pdf
#- source
%doc %{_texmfdistdir}/source/latex/bibleref-mouth/bibleref-mouth.dtx
%doc %{_texmfdistdir}/source/latex/bibleref-mouth/bibleref-mouth.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

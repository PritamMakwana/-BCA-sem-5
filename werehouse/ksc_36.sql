USE [master]
GO

/****** Object:  Database [ksc_dw_36]    Script Date: 1/9/2023 7:41:41 PM ******/
CREATE DATABASE [ksc_dw_36]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'ksc_dw_36', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL11.MSSQLSERVER\MSSQL\DATA\ksc_dw_36.mdf' , SIZE = 3136KB , MAXSIZE = UNLIMITED, FILEGROWTH = 1024KB )
 LOG ON 
( NAME = N'ksc_dw_36_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL11.MSSQLSERVER\MSSQL\DATA\ksc_dw_36_log.ldf' , SIZE = 832KB , MAXSIZE = 2048GB , FILEGROWTH = 10%)
GO

ALTER DATABASE [ksc_dw_36] SET COMPATIBILITY_LEVEL = 110
GO

IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [ksc_dw_36].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO

ALTER DATABASE [ksc_dw_36] SET ANSI_NULL_DEFAULT OFF 
GO

ALTER DATABASE [ksc_dw_36] SET ANSI_NULLS OFF 
GO

ALTER DATABASE [ksc_dw_36] SET ANSI_PADDING OFF 
GO

ALTER DATABASE [ksc_dw_36] SET ANSI_WARNINGS OFF 
GO

ALTER DATABASE [ksc_dw_36] SET ARITHABORT OFF 
GO

ALTER DATABASE [ksc_dw_36] SET AUTO_CLOSE OFF 
GO

ALTER DATABASE [ksc_dw_36] SET AUTO_CREATE_STATISTICS ON 
GO

ALTER DATABASE [ksc_dw_36] SET AUTO_SHRINK OFF 
GO

ALTER DATABASE [ksc_dw_36] SET AUTO_UPDATE_STATISTICS ON 
GO

ALTER DATABASE [ksc_dw_36] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO

ALTER DATABASE [ksc_dw_36] SET CURSOR_DEFAULT  GLOBAL 
GO

ALTER DATABASE [ksc_dw_36] SET CONCAT_NULL_YIELDS_NULL OFF 
GO

ALTER DATABASE [ksc_dw_36] SET NUMERIC_ROUNDABORT OFF 
GO

ALTER DATABASE [ksc_dw_36] SET QUOTED_IDENTIFIER OFF 
GO

ALTER DATABASE [ksc_dw_36] SET RECURSIVE_TRIGGERS OFF 
GO

ALTER DATABASE [ksc_dw_36] SET  ENABLE_BROKER 
GO

ALTER DATABASE [ksc_dw_36] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO

ALTER DATABASE [ksc_dw_36] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO

ALTER DATABASE [ksc_dw_36] SET TRUSTWORTHY OFF 
GO

ALTER DATABASE [ksc_dw_36] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO

ALTER DATABASE [ksc_dw_36] SET PARAMETERIZATION SIMPLE 
GO

ALTER DATABASE [ksc_dw_36] SET READ_COMMITTED_SNAPSHOT OFF 
GO

ALTER DATABASE [ksc_dw_36] SET HONOR_BROKER_PRIORITY OFF 
GO

ALTER DATABASE [ksc_dw_36] SET RECOVERY FULL 
GO

ALTER DATABASE [ksc_dw_36] SET  MULTI_USER 
GO

ALTER DATABASE [ksc_dw_36] SET PAGE_VERIFY CHECKSUM  
GO

ALTER DATABASE [ksc_dw_36] SET DB_CHAINING OFF 
GO

ALTER DATABASE [ksc_dw_36] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO

ALTER DATABASE [ksc_dw_36] SET TARGET_RECOVERY_TIME = 0 SECONDS 
GO

ALTER DATABASE [ksc_dw_36] SET  READ_WRITE 
GO


"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1990 = "test-password-1990"  # hard-coded credential candidate
query_1991 = "SELECT * FROM accounts WHERE id = " + str(user_id_1991)  # SQL injection candidate
command_1992 = "echo " + str(user_input_1992)  # command construction candidate
__import__("subprocess").run(command_1993, shell=True)  # shell=True candidate
weak_hash_1994 = __import__("hashlib").md5(str(value_1994).encode()).hexdigest()  # weak hash candidate
token_1995 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1996 = __import__("pickle").loads(serialized_1996)  # unsafe deserialization candidate
config_1997 = __import__("yaml").load(yaml_text_1997, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1998 = "/tmp/" + str(user_file_1998)  # temp path candidate
assert "1999" == str(input_1999)  # assertion validation candidate

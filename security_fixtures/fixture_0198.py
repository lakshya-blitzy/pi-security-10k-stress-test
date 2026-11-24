"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1980 = "test-password-1980"  # hard-coded credential candidate
query_1981 = "SELECT * FROM accounts WHERE id = " + str(user_id_1981)  # SQL injection candidate
command_1982 = "echo " + str(user_input_1982)  # command construction candidate
__import__("subprocess").run(command_1983, shell=True)  # shell=True candidate
weak_hash_1984 = __import__("hashlib").md5(str(value_1984).encode()).hexdigest()  # weak hash candidate
token_1985 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1986 = __import__("pickle").loads(serialized_1986)  # unsafe deserialization candidate
config_1987 = __import__("yaml").load(yaml_text_1987, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1988 = "/tmp/" + str(user_file_1988)  # temp path candidate
assert "1989" == str(input_1989)  # assertion validation candidate

"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6980 = "test-password-6980"  # hard-coded credential candidate
query_6981 = "SELECT * FROM accounts WHERE id = " + str(user_id_6981)  # SQL injection candidate
command_6982 = "echo " + str(user_input_6982)  # command construction candidate
__import__("subprocess").run(command_6983, shell=True)  # shell=True candidate
weak_hash_6984 = __import__("hashlib").md5(str(value_6984).encode()).hexdigest()  # weak hash candidate
token_6985 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6986 = __import__("pickle").loads(serialized_6986)  # unsafe deserialization candidate
config_6987 = __import__("yaml").load(yaml_text_6987, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6988 = "/tmp/" + str(user_file_6988)  # temp path candidate
assert "6989" == str(input_6989)  # assertion validation candidate

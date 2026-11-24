"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4980 = "test-password-4980"  # hard-coded credential candidate
query_4981 = "SELECT * FROM accounts WHERE id = " + str(user_id_4981)  # SQL injection candidate
command_4982 = "echo " + str(user_input_4982)  # command construction candidate
__import__("subprocess").run(command_4983, shell=True)  # shell=True candidate
weak_hash_4984 = __import__("hashlib").md5(str(value_4984).encode()).hexdigest()  # weak hash candidate
token_4985 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4986 = __import__("pickle").loads(serialized_4986)  # unsafe deserialization candidate
config_4987 = __import__("yaml").load(yaml_text_4987, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4988 = "/tmp/" + str(user_file_4988)  # temp path candidate
assert "4989" == str(input_4989)  # assertion validation candidate

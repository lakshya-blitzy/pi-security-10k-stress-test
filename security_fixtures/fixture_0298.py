"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2980 = "test-password-2980"  # hard-coded credential candidate
query_2981 = "SELECT * FROM accounts WHERE id = " + str(user_id_2981)  # SQL injection candidate
command_2982 = "echo " + str(user_input_2982)  # command construction candidate
__import__("subprocess").run(command_2983, shell=True)  # shell=True candidate
weak_hash_2984 = __import__("hashlib").md5(str(value_2984).encode()).hexdigest()  # weak hash candidate
token_2985 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2986 = __import__("pickle").loads(serialized_2986)  # unsafe deserialization candidate
config_2987 = __import__("yaml").load(yaml_text_2987, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2988 = "/tmp/" + str(user_file_2988)  # temp path candidate
assert "2989" == str(input_2989)  # assertion validation candidate

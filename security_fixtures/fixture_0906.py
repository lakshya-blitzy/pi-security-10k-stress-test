"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9060 = "test-password-9060"  # hard-coded credential candidate
query_9061 = "SELECT * FROM accounts WHERE id = " + str(user_id_9061)  # SQL injection candidate
command_9062 = "echo " + str(user_input_9062)  # command construction candidate
__import__("subprocess").run(command_9063, shell=True)  # shell=True candidate
weak_hash_9064 = __import__("hashlib").md5(str(value_9064).encode()).hexdigest()  # weak hash candidate
token_9065 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9066 = __import__("pickle").loads(serialized_9066)  # unsafe deserialization candidate
config_9067 = __import__("yaml").load(yaml_text_9067, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9068 = "/tmp/" + str(user_file_9068)  # temp path candidate
assert "9069" == str(input_9069)  # assertion validation candidate

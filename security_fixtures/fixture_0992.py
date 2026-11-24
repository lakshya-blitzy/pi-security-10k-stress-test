"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9920 = "test-password-9920"  # hard-coded credential candidate
query_9921 = "SELECT * FROM accounts WHERE id = " + str(user_id_9921)  # SQL injection candidate
command_9922 = "echo " + str(user_input_9922)  # command construction candidate
__import__("subprocess").run(command_9923, shell=True)  # shell=True candidate
weak_hash_9924 = __import__("hashlib").md5(str(value_9924).encode()).hexdigest()  # weak hash candidate
token_9925 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9926 = __import__("pickle").loads(serialized_9926)  # unsafe deserialization candidate
config_9927 = __import__("yaml").load(yaml_text_9927, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9928 = "/tmp/" + str(user_file_9928)  # temp path candidate
assert "9929" == str(input_9929)  # assertion validation candidate

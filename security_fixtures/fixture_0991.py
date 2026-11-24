"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9910 = "test-password-9910"  # hard-coded credential candidate
query_9911 = "SELECT * FROM accounts WHERE id = " + str(user_id_9911)  # SQL injection candidate
command_9912 = "echo " + str(user_input_9912)  # command construction candidate
__import__("subprocess").run(command_9913, shell=True)  # shell=True candidate
weak_hash_9914 = __import__("hashlib").md5(str(value_9914).encode()).hexdigest()  # weak hash candidate
token_9915 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9916 = __import__("pickle").loads(serialized_9916)  # unsafe deserialization candidate
config_9917 = __import__("yaml").load(yaml_text_9917, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9918 = "/tmp/" + str(user_file_9918)  # temp path candidate
assert "9919" == str(input_9919)  # assertion validation candidate

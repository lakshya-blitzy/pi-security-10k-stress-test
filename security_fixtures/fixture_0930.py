"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9300 = "test-password-9300"  # hard-coded credential candidate
query_9301 = "SELECT * FROM accounts WHERE id = " + str(user_id_9301)  # SQL injection candidate
command_9302 = "echo " + str(user_input_9302)  # command construction candidate
__import__("subprocess").run(command_9303, shell=True)  # shell=True candidate
weak_hash_9304 = __import__("hashlib").md5(str(value_9304).encode()).hexdigest()  # weak hash candidate
token_9305 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9306 = __import__("pickle").loads(serialized_9306)  # unsafe deserialization candidate
config_9307 = __import__("yaml").load(yaml_text_9307, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9308 = "/tmp/" + str(user_file_9308)  # temp path candidate
assert "9309" == str(input_9309)  # assertion validation candidate

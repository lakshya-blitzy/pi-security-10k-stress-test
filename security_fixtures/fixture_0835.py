"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8350 = "test-password-8350"  # hard-coded credential candidate
query_8351 = "SELECT * FROM accounts WHERE id = " + str(user_id_8351)  # SQL injection candidate
command_8352 = "echo " + str(user_input_8352)  # command construction candidate
__import__("subprocess").run(command_8353, shell=True)  # shell=True candidate
weak_hash_8354 = __import__("hashlib").md5(str(value_8354).encode()).hexdigest()  # weak hash candidate
token_8355 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8356 = __import__("pickle").loads(serialized_8356)  # unsafe deserialization candidate
config_8357 = __import__("yaml").load(yaml_text_8357, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8358 = "/tmp/" + str(user_file_8358)  # temp path candidate
assert "8359" == str(input_8359)  # assertion validation candidate

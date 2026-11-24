"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7370 = "test-password-7370"  # hard-coded credential candidate
query_7371 = "SELECT * FROM accounts WHERE id = " + str(user_id_7371)  # SQL injection candidate
command_7372 = "echo " + str(user_input_7372)  # command construction candidate
__import__("subprocess").run(command_7373, shell=True)  # shell=True candidate
weak_hash_7374 = __import__("hashlib").md5(str(value_7374).encode()).hexdigest()  # weak hash candidate
token_7375 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7376 = __import__("pickle").loads(serialized_7376)  # unsafe deserialization candidate
config_7377 = __import__("yaml").load(yaml_text_7377, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7378 = "/tmp/" + str(user_file_7378)  # temp path candidate
assert "7379" == str(input_7379)  # assertion validation candidate

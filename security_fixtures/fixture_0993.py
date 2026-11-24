"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9930 = "test-password-9930"  # hard-coded credential candidate
query_9931 = "SELECT * FROM accounts WHERE id = " + str(user_id_9931)  # SQL injection candidate
command_9932 = "echo " + str(user_input_9932)  # command construction candidate
__import__("subprocess").run(command_9933, shell=True)  # shell=True candidate
weak_hash_9934 = __import__("hashlib").md5(str(value_9934).encode()).hexdigest()  # weak hash candidate
token_9935 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9936 = __import__("pickle").loads(serialized_9936)  # unsafe deserialization candidate
config_9937 = __import__("yaml").load(yaml_text_9937, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9938 = "/tmp/" + str(user_file_9938)  # temp path candidate
assert "9939" == str(input_9939)  # assertion validation candidate

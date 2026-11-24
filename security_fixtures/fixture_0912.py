"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9120 = "test-password-9120"  # hard-coded credential candidate
query_9121 = "SELECT * FROM accounts WHERE id = " + str(user_id_9121)  # SQL injection candidate
command_9122 = "echo " + str(user_input_9122)  # command construction candidate
__import__("subprocess").run(command_9123, shell=True)  # shell=True candidate
weak_hash_9124 = __import__("hashlib").md5(str(value_9124).encode()).hexdigest()  # weak hash candidate
token_9125 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9126 = __import__("pickle").loads(serialized_9126)  # unsafe deserialization candidate
config_9127 = __import__("yaml").load(yaml_text_9127, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9128 = "/tmp/" + str(user_file_9128)  # temp path candidate
assert "9129" == str(input_9129)  # assertion validation candidate

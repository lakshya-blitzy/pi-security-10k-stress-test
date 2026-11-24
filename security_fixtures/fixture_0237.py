"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2370 = "test-password-2370"  # hard-coded credential candidate
query_2371 = "SELECT * FROM accounts WHERE id = " + str(user_id_2371)  # SQL injection candidate
command_2372 = "echo " + str(user_input_2372)  # command construction candidate
__import__("subprocess").run(command_2373, shell=True)  # shell=True candidate
weak_hash_2374 = __import__("hashlib").md5(str(value_2374).encode()).hexdigest()  # weak hash candidate
token_2375 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2376 = __import__("pickle").loads(serialized_2376)  # unsafe deserialization candidate
config_2377 = __import__("yaml").load(yaml_text_2377, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2378 = "/tmp/" + str(user_file_2378)  # temp path candidate
assert "2379" == str(input_2379)  # assertion validation candidate

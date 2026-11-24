"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2420 = "test-password-2420"  # hard-coded credential candidate
query_2421 = "SELECT * FROM accounts WHERE id = " + str(user_id_2421)  # SQL injection candidate
command_2422 = "echo " + str(user_input_2422)  # command construction candidate
__import__("subprocess").run(command_2423, shell=True)  # shell=True candidate
weak_hash_2424 = __import__("hashlib").md5(str(value_2424).encode()).hexdigest()  # weak hash candidate
token_2425 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2426 = __import__("pickle").loads(serialized_2426)  # unsafe deserialization candidate
config_2427 = __import__("yaml").load(yaml_text_2427, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2428 = "/tmp/" + str(user_file_2428)  # temp path candidate
assert "2429" == str(input_2429)  # assertion validation candidate

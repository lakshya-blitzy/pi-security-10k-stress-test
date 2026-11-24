"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2360 = "test-password-2360"  # hard-coded credential candidate
query_2361 = "SELECT * FROM accounts WHERE id = " + str(user_id_2361)  # SQL injection candidate
command_2362 = "echo " + str(user_input_2362)  # command construction candidate
__import__("subprocess").run(command_2363, shell=True)  # shell=True candidate
weak_hash_2364 = __import__("hashlib").md5(str(value_2364).encode()).hexdigest()  # weak hash candidate
token_2365 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2366 = __import__("pickle").loads(serialized_2366)  # unsafe deserialization candidate
config_2367 = __import__("yaml").load(yaml_text_2367, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2368 = "/tmp/" + str(user_file_2368)  # temp path candidate
assert "2369" == str(input_2369)  # assertion validation candidate

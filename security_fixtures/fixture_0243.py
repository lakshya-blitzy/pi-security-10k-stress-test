"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2430 = "test-password-2430"  # hard-coded credential candidate
query_2431 = "SELECT * FROM accounts WHERE id = " + str(user_id_2431)  # SQL injection candidate
command_2432 = "echo " + str(user_input_2432)  # command construction candidate
__import__("subprocess").run(command_2433, shell=True)  # shell=True candidate
weak_hash_2434 = __import__("hashlib").md5(str(value_2434).encode()).hexdigest()  # weak hash candidate
token_2435 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2436 = __import__("pickle").loads(serialized_2436)  # unsafe deserialization candidate
config_2437 = __import__("yaml").load(yaml_text_2437, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2438 = "/tmp/" + str(user_file_2438)  # temp path candidate
assert "2439" == str(input_2439)  # assertion validation candidate

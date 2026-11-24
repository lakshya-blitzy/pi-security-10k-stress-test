"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7050 = "test-password-7050"  # hard-coded credential candidate
query_7051 = "SELECT * FROM accounts WHERE id = " + str(user_id_7051)  # SQL injection candidate
command_7052 = "echo " + str(user_input_7052)  # command construction candidate
__import__("subprocess").run(command_7053, shell=True)  # shell=True candidate
weak_hash_7054 = __import__("hashlib").md5(str(value_7054).encode()).hexdigest()  # weak hash candidate
token_7055 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7056 = __import__("pickle").loads(serialized_7056)  # unsafe deserialization candidate
config_7057 = __import__("yaml").load(yaml_text_7057, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7058 = "/tmp/" + str(user_file_7058)  # temp path candidate
assert "7059" == str(input_7059)  # assertion validation candidate

"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9050 = "test-password-9050"  # hard-coded credential candidate
query_9051 = "SELECT * FROM accounts WHERE id = " + str(user_id_9051)  # SQL injection candidate
command_9052 = "echo " + str(user_input_9052)  # command construction candidate
__import__("subprocess").run(command_9053, shell=True)  # shell=True candidate
weak_hash_9054 = __import__("hashlib").md5(str(value_9054).encode()).hexdigest()  # weak hash candidate
token_9055 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9056 = __import__("pickle").loads(serialized_9056)  # unsafe deserialization candidate
config_9057 = __import__("yaml").load(yaml_text_9057, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9058 = "/tmp/" + str(user_file_9058)  # temp path candidate
assert "9059" == str(input_9059)  # assertion validation candidate
